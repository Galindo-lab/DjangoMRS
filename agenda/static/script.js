/**
 * Get the names of all months in a specified locale.
 *
 * @param {string} [locale='en-US'] - The locale to use for month names.
 * @param {string} [format='long'] - The format of the month names ('long' for full names, 'short' for short names).
 * @returns {string[]} An array of month names in the specified locale and format.
 */
const getMonthNames = (locale = 'en-US', format = 'long') => {
    // Create a date formatter for month names in the specified locale and format
    const monthFormatter = new Intl.DateTimeFormat(locale, {month: format});

    // Generate an array of month names by formatting dates for each month of the year
    return Array.from({length: 12}, (_, month) =>
        monthFormatter.format(new Date(2020, month, 1)) // 2020 is a leap year, ensuring all months are valid
    );
};

/**
 * Get the names of all weekdays in a specified locale.
 *
 * @param {string} [locale='en-US'] - The locale to use for weekday names.
 * @param {string} [format='long'] - The format of the weekday names ('long' for full names, 'short' for short names).
 * @returns {string[]} An array of weekday names in the specified locale and format.
 */
const getWeekdayNames = (locale = 'en-US', format = 'long') => {
    // Create a date formatter for weekday names in the specified locale and format
    const weekdayFormatter = new Intl.DateTimeFormat(locale, {weekday: format});

    // Generate an array of weekday names by formatting dates for each day of the week
    return Array.from({length: 7}, (_, day) =>
        weekdayFormatter.format(new Date(2020, 0, 5 + day)) // January 5, 2020 is a Sunday, ensuring the array starts from Sunday
    );
};