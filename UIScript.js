//Start of the nav bar codes

function decideToggle(){
    var navBar = document.getElementById("ReportSideBar").style.display

    if(navBar == "none"){
        openNav()
    } else{
        closeNav()
    }
}

function openNav(){
    document.getElementById("ReportSideBar").style.display = "block"
}
function closeNav(){
    document.getElementById("ReportSideBar").style.display = "none"
}
//End of Nav Bar Codes