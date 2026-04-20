import { z } from 'zod';
import { jsonResult } from './_format.js';
import * as core from '../core/wiki.js';

export function registerWikiTools(server) {
  server.tool(
    'wiki_search',
    'Semantic substring text search across all markdown files in the wiki and clippings, ignoring outputs and lint folders. Best way to find knowledge without loading huge indices.',
    {
      query: z.string().describe('Search query (will be split by spaces to find individual terms and full matches)'),
      limit: z.coerce.number().optional().describe('Max number of results to return (default 10)'),
    },
    async ({ query, limit }) => {
      try {
        return jsonResult(await core.searchWiki(query, limit || 10));
      } catch (err) {
        return jsonResult({ success: false, error: err.message }, true);
      }
    }
  );
}
