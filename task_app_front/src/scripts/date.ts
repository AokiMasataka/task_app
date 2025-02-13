export function stringToDate(date: string): Date {
    return new Date(date);
}

export function dateToString(date: Date): string {
    return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
}