"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const lib_1 = require("./lib");
/**
 *
 * This is the main Bitly module that returns an object of methods.  You need to pass in your
 * OAuth access token, as well as an optional config object. You are returned several helper
 * methods, as well as access to a method to pass any bitly api request to.
 *
 * For information on the data returned from the API, see the docs at
 * https://dev.bitly.com/api.html
 *
 * @module node-bitly
 * @type {function}
 * @param accessToken The access token, this from an OAuth session
 * @param config Optional config object
 * @returns A given Bitly response
 * @example
 * ```js
 *  const BitlyClient = require('bitly').BitlyClient;
 *  const bitly = new BitlyClient('<accessToken>');
 *  const myFunc = async(uri = 'https://github.com/tanepiper/node-bitly') => {
 *    try {
 *      return await bitly.shorten(uri);
 *   } catch(e) {
 *      throw e;
 *    }
 *  }
 * ```
 */
class BitlyClient {
    constructor(accessToken, config = {}) {
        this.accessToken = accessToken;
        this.config = config;
    }
    /**
     * This is used to get the summary of info about a given bitlink
     * Ref: https://dev.bitly.com/v4/#operation/getBitlink
     * @param  item ID, short Url, or hash
     * @return Summarized info about a given bitlink
     */
    getBitlink(item) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.bitlyRequest(`bitlinks/${lib_1.forceToBitlinkId(item)}`, {}, 'GET');
        });
    }
    /**
     * This is used to get the summary of info about a given bitlink
     * Legacy wrapper around getBitlink
     * @param item ID, short Url, or hash
     * @return Summarized info about a given bitlink
     */
    info(item) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.getBitlink(item);
        });
    }
    /**
     * Used to shorten a url
     * @param  longUrl The URL to be shortened
     * @return Shorten results
     */
    shorten(longUrl) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.bitlyRequest('shorten', { long_url: longUrl });
        });
    }
    /**
     * Request to expand urls and hashes
     * @param item ID, short Url, or hash
     * @return The results of the request
     */
    expand(item) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.bitlyRequest('expand', { bitlink_id: lib_1.forceToBitlinkId(item) });
        });
    }
    /**
     * Request to get clicks for urls and hashes
     * Defaults are per docs, and are the same result as if you call endpoint with no args
     * @param item ID, short Url, or hash
     * @param unit The unit of time for which to pull click stats
     * @param units The time units to pull data for
     * @param size How many results to limit the response to
     * @param unit_reference Optional - ISO-8601 timestamp, indicating the most recent time to pull stats for
     * @return The results of the request
     */
    clicks(item, unit = 'day', units = -1, size = 50, unit_reference) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.bitlyRequest(`bitlinks/${lib_1.forceToBitlinkId(item)}/clicks`, {
                unit,
                units,
                size,
                unit_reference
            }, 'GET');
        });
    }
    /**
     * Request to get clicks by minute for urls and hashes
     * @param item ID, short Url, or hash
     * @return Clicks by minute stats
     */
    clicksByMinute(item) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.clicks(item, 'minute');
        });
    }
    /**
     * Request to get clicks by day for urls and hashes
     * @param item ID, short Url, or hash
     * @return clicks by day stats
     */
    clicksByDay(item) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.clicks(item, 'day');
        });
    }
    /**
     * Lookup a single url
     * DEPRECATED
     * @param url The url to look up
     * @return Deprecated Error
     */
    lookup(url) {
        return __awaiter(this, void 0, void 0, function* () {
            return lib_1.throwDeprecatedErr('lookup', 'getBitlink');
        });
    }
    /**
     * Request referrers for a single url
     * @param item ID, short Url, or hash
     * @return Metrics by referrers
     */
    referrers(item) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.bitlyRequest(`bitlinks/${lib_1.forceToBitlinkId(item)}/referrers`, {}, 'GET');
        });
    }
    /**
     * Request countries for a single url
     * @param item ID, short Url, or hash
     * @returns Stats by countries
     */
    countries(item) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.bitlyRequest(`bitlinks/${lib_1.forceToBitlinkId(item)}/countries`, {}, 'GET');
        });
    }
    /**
     * Perform any bitly API request using a method name and passed data object
     * @param method The method name to be called on the API. Not to be confused with reques method (aka HTTP verb)
     * @param data The data object to be passed. Keys should be query or body parameters.
     * @param reqMethod The HTTP request method to be used (aka *HTTP Verb*)
     * @typeparam ResponseType - The expected response type
     * @return The bitly request return data
     */
    bitlyRequest(method, data, reqMethod = 'POST') {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                return yield lib_1.doRequest(this.accessToken, method, data, this.config, reqMethod);
            }
            catch (e) {
                const err = e;
                if (err.response) {
                    throw err.response.data;
                }
                throw err;
            }
        });
    }
}
exports.BitlyClient = BitlyClient;
/**
 * Bitly object definition
 * @typedef {object} Bitly
 * @property {Function} getBitlink Function that is used to get the summary of info about a given bitlink.
 * @property {Function} shorten Function that takes a url and shortens it. Accepts valid URL.
 * @property {Function} expand Function that gets long urls for short urls. Accepts valid Bitlink.
 * @property {Function} clicks Function that gets the number of clicks of short urls. Accepts valid Bitlink.
 * @property {Function} clicksByMinute Function that gets the number of clicks by minute for short urls. Accepts valid Bitlink.
 * @property {Function} clicksByDay Function that gets the number of clicks by day for short urls. Accepts valid Bitlink.
 * @property {Function} lookup !!! - DEPRECATED --- !!! Function that takes a url looks up data. Accepts valid URL.
 * @property {Function} info Function that takes a url and gets info. Accepts valid Bitlink.
 * @property {Function} referrers Function that gets referrers for urls. Accepts valid Bitlink.
 * @property {Function} countries Function that gets click by countries for urls. Accepts valid Bitlink.
 * @property {Function} bitlyRequest Function that allows you to to any bitly request
 */
//# sourceMappingURL=bitly.js.map