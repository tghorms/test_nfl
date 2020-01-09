//pass information for the Machine Learning model.
function simplerun() {
    
    var Home_team = document.getElementById("Home_team").value
    var Away_team = document.getElementById("Away_team").value
    var Book_Total = +document.getElementById("BookTotal").value
    //todo: make a thing that will clear the over under input  before the run.

    console.log(Home_team)
    console.log(Away_team)
    console.log(Book_Total)

    d3.json("/x").then((response) => {
        document.getElementById("vince").innerHTML=response
    })     
}
//creates the team listing on the webpage.
function init() {
    console.log("vince")
    //Team_Call("#Home_team")
    //Team_Call("#Away_team")
}

//function to call to create teams
function Team_Call(str_IDselector) {
    var home_selector = d3.select(str_IDselector)
    d3.json("/y").then((xx) => {
        xx.forEach((sample) => {
            home_selector
                .append("option")
                .text(sample.Home_Team)
                .property("value", sample.ID)
        })
    })
}

//initialize the selectors
init();