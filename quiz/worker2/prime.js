function Prime(num) {
    if (num < 2) return false; 
    for (let i =2; i<= num /2; i++) {
        if(num % 1 == 0) {
            return false; 
        }
    }
    return true; 
}
self.onmessage = function(e) {
    let number = e.data; 

    output = number; 
    output += (Prime(number)) ? " is Prime Number " : " is not Prime Number "; 
    // 소수 판결 결과 전송
    self.postMessage(output); 
}