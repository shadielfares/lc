impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut s = s.trim();
        let mut length: i32 = 0;
        for c in s.chars().rev() {
            if c != ' ' {
                length += 1;
            } else{
                break;
            }
        }        
        return length;
    }
}