//Start of the nav bar codes

//Decide how to toggle nav bar
function decideToggle(){
    var navBar = document.getElementById("ReportSideBar").style.display

    if(navBar == "none"){
        openNav()
    } else{
        closeNav()
    }
}

//Make the nav visible
function openNav(){
    document.getElementById("ReportSideBar").style.display = "block"
    
    let date = grabDate()
    document.getElementById("date").innerHTML = date
}

//Make nav invisable
function closeNav(){
    document.getElementById("ReportSideBar").style.display = "none"
}
//End of Nav Bar Codes

//Start of Date Time Entry
//The date created for each of the new routes
function grabDate(){
    const holdingDate = new Date()
    
    //Grab all parts of date
    var day =  "" + holdingDate.getDay()
    var month = "" + holdingDate.getMonth()
    var year = "" + holdingDate.getFullYear()
    var hour = "" + holdingDate.getHours()
    var min = "" + holdingDate.getMinutes()
    var sec = "" + holdingDate.getSeconds()

    //Combine
    var combinedDate = "" + year + "-" + month.padStart(2, '0') + "-" + day.padStart(2, '0')
    var combinedTime = "" + hour.padStart(2, '0') + ":" + min.padStart(2, '0') + ":" + sec.padStart(2, '0')

    var combinedAll = combinedDate + " " + combinedTime
    
    //document.getElementById("TESTER").innerHTML = combinedAll // Test Line

    return combinedAll
 }

//End of Date/Time Entry

//Start of dupliating route options

//End of route dups