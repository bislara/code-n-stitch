"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * Type Guards
 */
function isBitlyLink(response) {
    return 'link' in response && 'id' in response && 'long_url' in response;
}
exports.isBitlyLink = isBitlyLink;
function isBitlyErrResponse(response) {
    return 'message' in response && 'resource' in response;
}
exports.isBitlyErrResponse = isBitlyErrResponse;
//# sourceMappingURL=types.js.map