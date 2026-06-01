/**
 * rehype plugin: tag Amazon affiliate links with class="noskim".
 *
 * Skimlinks (loaded site-wide) rewrites outbound merchant links to inject ITS
 * own affiliate tracking, which would skim a cut of — or fully divert — the
 * commission on our direct Amazon Associates links (tag=errorcodefixes-20).
 * Skimlinks explicitly skips any link carrying the `noskim` class, so adding it
 * to every Amazon link keeps 100% of the Associates commission with us.
 *
 * This replaces the dashboard-side "exclude amazon.com" TODO with a durable,
 * in-code guarantee that also covers every future article. Dependency-free.
 */
export default function rehypeNoskim() {
  return tree => {
    const walk = node => {
      if (node && node.type === "element" && node.tagName === "a") {
        const href = node.properties && node.properties.href;
        if (typeof href === "string" && /(^|\.)amazon\.(com|co\.[a-z]{2}|ca|de|fr|it|es)\b/i.test(href)) {
          const cls = node.properties.className;
          const arr = Array.isArray(cls) ? cls : cls ? [String(cls)] : [];
          if (!arr.includes("noskim")) arr.push("noskim");
          node.properties.className = arr;
        }
      }
      if (node && Array.isArray(node.children)) for (const c of node.children) walk(c);
    };
    walk(tree);
  };
}
