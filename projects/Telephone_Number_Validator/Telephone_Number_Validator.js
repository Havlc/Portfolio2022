function telephoneCheck(str) {

	let reg = /^(1\s?)?(\(([0-9]{3})\)|(([0-9]{3})))[-\s]?[0-9]{3}[-\s]?[0-9]{4}$/gi

	return reg.test(str);

}

console.log(telephoneCheck("555)-555-5555"))