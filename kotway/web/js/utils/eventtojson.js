

/**
 * Converts an event class to a dict.
 * @param {*} event 
 * @returns 
 */
export function eventToJSON(event) {
  const jsonableData = {};

  if (event.target && 'value' in event.target) {
    jsonableData.inputValue = event.target.value;
  }

  // for...in retrieves properties along the prototype chain (where event props live)
  for (const key in event) {
    try {
      const value = event[key];
      const type = typeof value;

      // 1. Skip functions, symbols, and undefined
      if (type === 'function' || type === 'symbol' || type === 'undefined') {
        continue;
      }

      // 2. Skip DOM nodes, window objects, or complex objects to prevent circular references
      if (
        value !== null &&
        (type === 'object' || type === 'function') &&
        (value instanceof Node || value instanceof Window || value === event)
      ) {
        continue;
      }

      // 3. Test if the value can actually be stringified safely
      JSON.stringify(value);
      
      jsonableData[key] = value;
    } catch (e) {
      // Catches non-serializable values, circular references, or getter errors
      continue;
    }
  }

  return jsonableData;
}