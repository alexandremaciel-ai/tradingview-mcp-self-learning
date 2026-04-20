#!/usr/bin/env node
import { searchWiki } from '../../src/core/wiki.js';

const query = process.argv.slice(2).join(' ');

if (!query) {
  console.error('Usage: node wiki-search.js "search query"');
  process.exit(1);
}

async function run() {
  try {
    const res = await searchWiki(query, 10);
    console.log(`\n🔍 Found ${res.results_found} matching documents for "${query}"\n`);
    
    if (res.results_found === 0) {
      console.log('No matches found.');
      return;
    }

    res.top_matches.forEach((m, idx) => {
      console.log(`[${idx + 1}] Score: ${m.score} — ${m.path}`);
      console.log(`    > ${m.snippet}\n`);
    });
  } catch (err) {
    console.error('Error:', err.message);
    process.exit(1);
  }
}

run();
