/**
 * remark plugin: support Pandoc-style `{#custom-id}` at the end of a heading.
 *
 * Astro's GFM markdown pipeline does NOT understand this syntax, so headings
 * authored as `## Step-by-Step Fix {#fix}` were rendering the literal `{#fix}`
 * as VISIBLE text AND folding it into the auto-generated slug
 * (e.g. id="how-to-fix-alarm-506-how-to-fix"). That broke the in-page
 * "Jump to Fix" / "View Parts" anchors on hundreds of articles and looked like
 * a quality defect to readers.
 *
 * This strips the trailing `{#id}` token from the heading text and pins the
 * heading id to exactly that value, so both the visible cruft disappears and
 * the `#fix` / `#step-by-step-fix` / `#parts` anchor links resolve.
 *
 * Dependency-free (no unist-util-visit) so it adds nothing to the lockfile.
 */
export default function remarkHeadingIds() {
  return tree => {
    const walk = node => {
      if (
        node &&
        node.type === "heading" &&
        Array.isArray(node.children) &&
        node.children.length
      ) {
        const last = node.children[node.children.length - 1];
        if (last && last.type === "text" && typeof last.value === "string") {
          const m = last.value.match(/\s*\{#([A-Za-z0-9_-]+)\}\s*$/);
          if (m) {
            last.value = last.value.slice(0, m.index).replace(/\s+$/, "");
            node.data = node.data || {};
            node.data.id = m[1];
            node.data.hProperties = { ...(node.data.hProperties || {}), id: m[1] };
            if (last.value === "") node.children.pop();
          }
        }
      }
      if (node && Array.isArray(node.children)) {
        for (const child of node.children) walk(child);
      }
    };
    walk(tree);
  };
}
