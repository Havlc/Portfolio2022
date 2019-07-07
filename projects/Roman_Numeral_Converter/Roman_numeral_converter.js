function convertToRoman(num) {
	let newNum = num.toString()
	console.log(newNum)
	let one = Number(newNum[newNum.length-1]);
	let dec = Number(newNum[newNum.length-2]);
	let hun = Number(newNum[newNum.length-3]);
	let tho = Number(newNum[newNum.length-4]);

	let c1 = "I";
	let c5 = "V";
	let c10 = "X";
	let c100 = "C";
	let c500 = "D";
	let c1000 = "M";

	let result = "";

	//thousands
	if (tho >= 0 && tho < 4){
		result += c1000.repeat(tho);
	}
	//hundred
	if( hun ===9){
		result += "CM";
	}
	else if (hun >=5 && hun <9){
		result += "D"+c100.repeat(hun-5);
	}
	else if(hun===4){
		result +="CD";
	}
	else if (hun>=0 && hun<4){
		result += c100.repeat(hun);
	}
	//decimals
	if(dec===9){
		result += "XC";
	}
	else if (dec>=5 && dec<9){
		result += "L"+c10.repeat(dec-5);
	}
	else if(dec===4){
		result +="XL";
	}
	else if (dec>=0 && dec<4){
		result += c10.repeat(dec);
	}
	//ones
	if(one===9){
		result += "IX";
	}
	else if (one>=5 && one<9){
		result += "V"+c1.repeat(one-5);
	}
	else if(one===4){
		result +="IV";
	}
	else if (one>0 && one<4){
		result += c1.repeat(one);
	}
	else {
		result += ""
	}
	return result;
	}

console.log(convertToRoman(3999))
