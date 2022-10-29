//Start of the nav bar codes

function decideToggle(){
    var navBar = document.getElementById("ReportSideBar").style.direction

    if(document.getElementById("ReportSideBar").style.direction == "none"){
        closeNav()
    } else{
        openNav()
    }
}

function openNav(){
    document.getElementById("ReportSideBar").style.width = "100%"
    document.getElementById("ReportSideBar").style.direction = "Block"
        

}
function closeNav(){
    document.getElementById("ReportSideBar").style.direction = "none"
}
//End of Nav Bar Codes