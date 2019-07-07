function palindrome(str) {
	let reg = /[a-zA-Z0-9]/gi
	let low = str.match(reg).join("").toLowerCase();
	let reverse = [];

	for (let i=low.length-1; i>=0;i--){
		reverse.push(low[i]);
	}

	let compare = reverse.join("")
	if (compare === low){
		return true;
	}
	return false;
}

palindrome("eye");