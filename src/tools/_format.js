/**
 * Shared MCP response formatting helper.
 * All tool files use this instead of manually constructing MCP responses.
 */
export function jsonResult(obj, isError = false) {
  return {
    content: [{ type: 'text', text: JSON.stringify(obj, null, 2) }],
    ...(isError && { isError: true }),
  };
}

/**
 * Wraps a core function as an MCP tool handler: runs it with the incoming args,
 * returns jsonResult on success, and a uniform error result on throw.
 * `errExtra` adds extra fields (e.g. a hint) to the error payload.
 */
export function handle(fn, errExtra) {
  return async (args) => {
    try { return jsonResult(await fn(args)); }
    catch (err) { return jsonResult({ success: false, error: err.message, ...errExtra }, true); }
  };
}
