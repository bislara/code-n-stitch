/// <reference types="node" />
import { UrlWithStringQuery } from 'url';
import { BitlyConfig, BitlyQueryParams, BitlyReqMethod, BitlyResponse } from './types';
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
export declare function generateUrl(method: string, data?: BitlyQueryParams, config?: BitlyConfig, reqMethod?: BitlyReqMethod): UrlWithStringQuery;
/**
 * Method called to generate a url and call the request
 * @param bearer The request accessToken
 * @param method The method to be called on Bitly
 * @param data A data object with key=>value pairs mapped to request parameters
 * @param config A object that overrides the default values for a request
 * @param reqMethod The HTTP Method to use
 * @returns The request result object
 */
export declare function doRequest(bearer: string, method: string, data: BitlyQueryParams, config: BitlyConfig, reqMethod?: BitlyReqMethod): Promise<BitlyResponse>;
/**
 * Function to check through an array of items to check for short urls or hashes
 * If only passed one item, put in array for url checking
 * @param  unsortedItems The array of items to be checked
 * @param  result The query object
 * @return Sorted shortUrls and hashes
 */
export declare function sortUrlsAndHash(unsortedItems: string | string[], result?: BitlyQueryParams): BitlyQueryParams;
/**
 * Function to force a string that *could* be an old-style hash to the new ID style
 * This is allow backward-compatibility with IDs produced by V3, and perhaps stored in users' DBs
 * @param hashIdOrLink An old style hash, or v4 bitly id (bitlink), or full bitly link
 * @returns Bitlink (domain + hash) formatted ID
 * @private
 */
export declare function forceToBitlinkId(hashIdOrLink: string): string;
export declare const BitlyIdPattern: RegExp;
export declare const BitlyHashPattern: RegExp;
/**
 * Throw a deprecated error
 * @param methodName Bitly method name
 * @param replacementMethod Method that might be a suitable replacement
 * @param helpUrl URL with more info
 * @private
 */
export declare function throwDeprecatedErr(methodName: string, replacementMethod?: string, helpUrl?: string): void;
