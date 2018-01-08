
function registerBike() {
    var bikemodel = document.getElementById("mfr").value;
    var serialnumber = document.getElementById("serial_number").value;
    var bikecode = serialnumber.toUpperCase()+"-"+bikemodel;

    window.alert(bikecode);
}
