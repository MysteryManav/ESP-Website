function Scheduler(data, directoryEl, matrixEl, garbageEl) {
    this.directory = new Directory(data.sections, directoryEl, data.schedule_assignments)
    this.matrix = new Matrix(data.timeslots, data.rooms, data.schedule_assignments, data.sections, matrixEl, garbageEl)
    this.render = function(){
	this.directory.render()
	this.matrix.render()
    }
}
