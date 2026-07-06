import type { CollectionEntry } from "astro:content";
import getSortedPosts from "./getSortedPosts";
import { NOINDEX_SLUGS } from "@/data/noindex-slugs";

// Sorted, published posts EXCLUDING the noindexed prune set. Use for every
// listing / navigation surface (home, archive + pagination, tags, brand +
// equipment hubs, related, rss, author) so the CRAWLABLE site is the
// ~1,185-page quality core, not the 5,680-page farm. This is what removes the
// pruned pages from internal link discovery (the piece noindex alone can't do,
// since AdSense/Google crawlers follow links regardless of the index).
//
// Do NOT use this for [...slug] prev/next — that needs the full sorted set so a
// noindexed page can still resolve its neighbours instead of breaking findIndex.
const getListablePosts = (posts: CollectionEntry<"blog">[]) =>
  getSortedPosts(posts).filter(post => !NOINDEX_SLUGS.has(post.id));

export default getListablePosts;
