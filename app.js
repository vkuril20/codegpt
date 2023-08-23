const submitButton = document.querySelector('#submit')
const outPutElement = document.querySelector('#output')
const inputElement = document.querySelector('input')
const historyElement = document.querySelector('.history')
const buttonElement = document.querySelector('button')
var lastquery=""
var messagelist=[{role: "system",content: "You are a helpful assistant."}]

function changeInput(value){
    console.log('changing input')
    console.log(value)
    inputElement.value=value
}
historyElement.addEventListener('click',()=> changeInput(event.target.textContent))

async function getMessage() {
    console.log('clicked')
    messagelist=messagelist.concat({role:"user", content: inputElement.value})
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            messages: messagelist,
        })
    }
    try {
        const response = await fetch('http://127.0.0.1:8000/posting_data/', options)
        const data = await response.json()
        console.log(data)
        messagelist=messagelist.concat({role:"assistant",content:data.message.content})
        if(response.status==200){
            //Creating a history element
            lastquery=inputElement.value
            const pElement= document.createElement('p')
            pElement.textContent = lastquery
            historyElement.append(pElement)

            //Creating a output element
            const selement=document.createElement('p')
            selement.textContent=inputElement.value
            console.log(selement.textContent)
            outPutElement.append(selement)

            const position =data.message.content.search("user:")
            if(position==-1){
                var finalstr=data.message.content
            }
            else{
                var finalstr=data.message.content.substring(0,position)
            }
            selement.textContent=finalstr
            console.log(finalstr)
            outPutElement.append(selement)
            console.log('Added into output stream')

        }
    } catch (error) {
        console.error(error)
    }
    clearInput();
}

submitButton.addEventListener('click', getMessage)
function clearInput(){
    inputElement.value =''
}
buttonElement.addEventListener('click',newchat)
async function newchat(){
    console.log("newchat")
    outPutElement.value=''
    lastquery=""
    messagelist=[{role: "system",content: "You are a helpful assistant."}]
    clearInput();
}
