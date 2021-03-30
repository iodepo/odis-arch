// Helper function: See if an object is undefine
export function getSafe(fn) {
	try {
		return fn();
	} catch (e) {
		return undefined;
	}
}
