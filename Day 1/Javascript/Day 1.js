// Advent of Code 2020
// Day 1

// Open the given input page at https://adventofcode.com/2020/day/1/input and run these scripts in dev tools console

// Part1

(() => {
    const n = document.body.innerText.split('\n').map(Number),
        l = n.length;
    for(let i = 0; i < l; ++i) {
        for(let j = 0; j < l; ++j) {
                if(n[j] + n[i] === 2020) return (n[j] * n[i])
            }
        }
    }
)();


// Part 2
(() => {
    const n = document.body.innerText.split('\n').map(Number),
        l = n.length;
    for(let i = 0; i < l; ++i) {
        for(let j = 0; j < l; ++j) {
            for(let k = 0; k < l; ++k) {
                if(n[k] + n[j] + n[i] === 2020) return (n[k] * n[j] * n[i])
            }
        }
    }
})();
