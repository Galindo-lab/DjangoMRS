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

/**
 * Get the weeks in a given month of a given year. Each week is represented by an array of two dates: Monday and Sunday.
 *
 * @param {number} year - The year for which to get the weeks.
 * @param {number} month - The month (0-11) for which to get the weeks.
 * @returns {Array.<[Date, Date]>} An array of weeks, each represented by an array of two dates (Monday and Sunday).
 */
const getWeeksInMonth = (year, month) => {
    const MS_PER_DAY = 24 * 60 * 60 * 1000;

    let startDate = new Date(year, month, 1);
    let endDate = new Date(year, month + 1, 0);

    startDate = new Date(startDate.getTime() + ((startDate.getDay() + 6) % 7) * MS_PER_DAY);
    endDate = new Date(endDate.getTime() + (7 - endDate.getDay()) * MS_PER_DAY);

    const numberOfWeeks = Math.floor((endDate - startDate) / (7 * MS_PER_DAY)) + 1;

    return Array.from({length: numberOfWeeks}, (_, i) => {
        const monday = new Date(startDate.getTime() + i * 7 * MS_PER_DAY);
        const sunday = new Date(monday.getTime() + 6 * MS_PER_DAY);
        return [monday, sunday];
    }).filter(week => week[0].getMonth() === month || week[1].getMonth() === month);
};

/**
 * Format a date range in a human-readable format.
 *
 * @param {Date} start - The start date of the range.
 * @param {Date} end - The end date of the range.
 * @param {string} [locale='es-ES'] - The locale to use for formatting the dates.
 * @returns {string} The formatted date range.
 */
const formatDateRange = (start, end, locale = 'en-US') => {
    const startDay = start.getDate();
    const startMonthName = start.toLocaleDateString(locale, {day: 'numeric', month: 'short'});
    const endMonthName = end.toLocaleDateString(locale, {day: 'numeric', month: 'short'});

    return start.getMonth() === end.getMonth() ?
        `${startDay} - ${endMonthName}` :    // 1 - 7 de julio
        `${startMonthName} - ${endMonthName}`; // 30 de julio - 5 de agosto
}