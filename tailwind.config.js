const defaultTheme = require('tailwindcss/defaultTheme');
const colors = require('tailwindcss/colors');

module.exports = {
	content: ["./templates/**/*.html"],
	theme: {
		extend: {},
	},
	plugins: [require('@tailwindcss/forms')],
};
