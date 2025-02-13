import { state } from '../../scripts/const.ts';

export const items = Object.entries(state).map(([text, value]) => {
    return {
        text,
        value
    }
});


export const prioritys = [
    {text: "low", value: 0},
    {text: "midiam", value: 1},
    {text: "high", value: 2},
];

export const colors = {
    0: "blue",
    1: "green",
    2: "red"
}