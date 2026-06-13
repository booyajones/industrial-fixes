import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";
import { SITE } from "@/config";

export const BLOG_PATH = "src/data/blog";

const blog = defineCollection({
  loader: glob({ pattern: "**/[^_]*.md", base: `./${BLOG_PATH}` }),
  schema: ({ image }) =>
    z.object({
      author: z.string().default(SITE.author),
      pubDatetime: z.date(),
      modDatetime: z.date().optional().nullable(),
      title: z.string(),
      featured: z.boolean().optional(),
      draft: z.boolean().optional(),
      tags: z.array(z.string()).default(["others"]),
      ogImage: image().or(z.string()).optional(),
      description: z.string(),
      canonicalURL: z.string().optional(),
      hideEditPost: z.boolean().optional(),
      timezone: z.string().optional(),
      // Diagnosis Command Center fields (optional; only on deep code pages).
      most_likely_cause: z.string().optional(),
      likelihood: z.string().optional(),
      diy_or_pro: z.enum(["diy", "pro"]).optional(),
      money_part: z.string().optional(),
      // No-buy verdict fields (the cost-fork lever). All optional so the verdict
      // renders qualitatively from most_likely_cause + money_part alone, and
      // sharpens automatically as the generator/backfill fills these in.
      free_checks: z.array(z.string()).optional(), // 2–3 free checks to do first
      part_price: z.string().optional(),           // typical street price, e.g. "$45–70"
      no_buy_pct: z.string().optional(),           // grounded share that are a $0/cheap fix, e.g. "70%"
    }),
});

export const collections = { blog };
