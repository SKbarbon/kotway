

export function findControlByUuid(uuid, controls) {
    if (!Array.isArray(controls)) return null;
    
    for (const c of controls) {
        if (c.uuid === uuid) {
            return c;
        }

        
        if (Array.isArray(c.controls)) {
            const found = findControlByUuid(uuid, c.controls);
            if (found !== null) {
                return found;
            }
        }
    }

    return null;
}