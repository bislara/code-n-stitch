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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const axios_1 = __importDefault(require("axios"));
const url_1 = require("url");
const isUri = require('valid-url').isUri;
/**
 * The internal library of node-bitly
 * @module node-bitly.lib
 * @private
 */
const DEFAULT_OPTIONS = {
    apiUrl: 'api-ssl.bitly.com',
    apiVersion: 'v4',
    domain: 'bit.ly',
    format: 'json',
    debug: false
};
/**
 * Generates a valid URL for a GET request to the Bit.ly API
 * @param method The method to call
 * @param data a data object specifying bit.ly keys for your method
 * @param config A custom config object to overide values
 * @param reqMethod The HTTP request method
 * @returns parsed generated URL
 * @private
 *
 * @example
 * ```js
 * generateUrl({method: 'shorten', accessKey: 'myaccessKey', data: { longUrl: 'https://github.com/tanepiper/node-bitly' } });
 * ```
 */
function generateUrl(method, data = {}, config = {}, reqMethod = 'POST') {
    let formatUrlOptions = {
        protocol: "https",
        hostname: config.apiUrl || DEFAULT_OPTIONS.apiUrl,
        pathname: `/${config.apiVersion || DEFAULT_OPTIONS.apiVersion}/${method}`
    };
    if (reqMethod === 'GET') {
        formatUrlOptions.query = data;
    }
    return url_1.parse(url_1.format(formatUrlOptions));
}
exports.generateUrl = generateUrl;
/**
 * Method called to generate a url and call the request
 * @param bearer The request accessToken
 * @param method The method to be called on Bitly
 * @param data A data object with key=>value pairs mapped to request parameters
 * @param config A object that overrides the default values for a request
 * @param reqMethod The HTTP Method to use
 * @returns The request result object
 */
function doRequest(bearer, method, data, config, reqMethod = 'POST') {
    return __awaiter(this, void 0, void 0, function* () {
        const url = url_1.format(generateUrl(method, data, config, reqMethod));
        const requestOptions = {
            method: reqMethod,
            url,
            headers: {
                Authorization: bearer
            },
            responseType: 'json'
        };
        if (reqMethod !== 'GET') {
            const body = Object.assign({
                domain: config.domain || DEFAULT_OPTIONS.domain,
                long_url: data.long_url
            });
            Object.keys(data || []).forEach((key) => (body[key] = data[key]));
            requestOptions.data = body;
            requestOptions.headers['Content-Type'] = 'application/json';
        }
        try {
            const req = yield axios_1.default(requestOptions);
            if (config.debug) {
                console.log(req);
            }
            return req.data;
        }
        catch (error) {
            if (config.debug) {
                console.log(error);
            }
            throw error;
        }
    });
}
exports.doRequest = doRequest;
/**
 * Function to check through an array of items to check for short urls or hashes
 * If only passed one item, put in array for url checking
 * @param  unsortedItems The array of items to be checked
 * @param  result The query object
 * @return Sorted shortUrls and hashes
 */
function sortUrlsAndHash(unsortedItems, result = { shortUrl: [], hash: [] }) {
    result.shortUrl = result.shortUrl || [];
    result.hash = result.hash || [];
    (Array.isArray(unsortedItems) ? unsortedItems : [unsortedItems]).map(item => isUri(item)
        ? result.shortUrl.push(item)
        : typeof item === 'string' && result.hash.push(item));
    return result;
}
exports.sortUrlsAndHash = sortUrlsAndHash;
/**
 * Function to force a string that *could* be an old-style hash to the new ID style
 * This is allow backward-compatibility with IDs produced by V3, and perhaps stored in users' DBs
 * @param hashIdOrLink An old style hash, or v4 bitly id (bitlink), or full bitly link
 * @returns Bitlink (domain + hash) formatted ID
 * @private
 */
function forceToBitlinkId(hashIdOrLink) {
    // Old-style hash
    if (/^[A-z0-9]{6,}$/.test(hashIdOrLink)) {
        return `bit.ly/${hashIdOrLink}`;
    }
    // Bit.ly ID, or http/s prefixed bitly
    if (exports.BitlyHashPattern.test(hashIdOrLink)) {
        const hash = exports.BitlyHashPattern.exec(hashIdOrLink)[1];
        return `bit.ly/${hash}`;
    }
    // For everything else, or maybe custom bitlinks
    return hashIdOrLink;
}
exports.forceToBitlinkId = forceToBitlinkId;
exports.BitlyIdPattern = /.*bit.ly\/([A-z0-9_-]{6,})$/i;
exports.BitlyHashPattern = /\/([A-z0-9_-]{6,})$/;
/**
 * Throw a deprecated error
 * @param methodName Bitly method name
 * @param replacementMethod Method that might be a suitable replacement
 * @param helpUrl URL with more info
 * @private
 */
function throwDeprecatedErr(methodName, replacementMethod, helpUrl) {
    let errMsg = `DEPRECATED: "${methodName}" is no longer supported by the Bitly API.`;
    if (replacementMethod) {
        errMsg += `\nPlease evaluate ${replacementMethod} as a replacement.`;
    }
    if (helpUrl) {
        errMsg += `\nFor more info, see ${helpUrl}`;
    }
    throw new Error(errMsg);
}
exports.throwDeprecatedErr = throwDeprecatedErr;
//# sourceMappingURL=lib.js.map