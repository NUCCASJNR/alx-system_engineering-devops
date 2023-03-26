export default class HolbertonClass {
	  constructor(size, location) {
		      this._size = size;
		      this._location = location;
		    }

	  valueOf() {
		      return this._size;
		    }

	  toString() {
		      return this._location;
		    }
}

const myClass = new HolbertonClass(20, 'San Francisco');
console.log(myClass.valueOf()); // Output: 20
console.log(myClass.toString())
