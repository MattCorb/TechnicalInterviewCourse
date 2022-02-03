/**
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise. Use a dictionary.
 * 
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
 * typically using all the original letters exactly once.
 * 
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 * 
 * Input: s = "rat", t = "car"
 * Output: false
 * 
 * Source: https://leetcode.com/problems/valid-anagram/
 */

const s = 'anagram'
const t = 'nagaram'

function anagram(x,y){
    ref = {}
    out = true
    for(let i = 0 ; i < x.length; i++){
        ref[x[i]] = 1
    }
    
    for (let j = 0 ; j < y.length; j++){
        if(!(Object.keys(ref).includes(y[j]))){
            out = false
        }
       
    }
    return  out
}


console.log(anagram(s,t))