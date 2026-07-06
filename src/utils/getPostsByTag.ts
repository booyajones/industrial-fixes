import type { CollectionEntry } from "astro:content";
import getListablePosts from "./getListablePosts";
import { slugifyAll } from "./slugify";

const getPostsByTag = (posts: CollectionEntry<"blog">[], tag: string) =>
  getListablePosts(
    posts.filter(post => slugifyAll(post.data.tags).includes(tag))
  );

export default getPostsByTag;
