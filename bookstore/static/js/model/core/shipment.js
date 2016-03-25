function shipment(address, type, promisedDate, deliveredDate){
	this.address = address
	this.type = type
	this.promisedDate = promisedDate
	this.deliveredDate = deliveredDate || null
}