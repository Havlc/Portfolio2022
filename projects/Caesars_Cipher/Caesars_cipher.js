function rot13(str) {
	console.log(str)
	let alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
	let cip = ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M"];
	let reg = /[^A-Z]/gi
	let result = "";
	for(let i=0;i<str.length;i++){
		if(reg.test(str[i])){
			result+=str[i];
		} else {
			let c = alpha.indexOf(str[i])
			result += cip[c];
		}
	}
	return result;
}

console.log(rot13("UVER ZR!"));