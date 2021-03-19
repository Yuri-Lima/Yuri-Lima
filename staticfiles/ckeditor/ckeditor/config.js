/**
 * @license Copyright (c) 2003-2020, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.allowedContent = false;
	config.language = 'en';
	// config.uiColor = '#AADC6E';
	config.extraPlugins = 'youtube,codesnippet,widget';
	config.youtube_responsive = true;
	config.youtube_controls = true;

};
