const express = require('express');
const app = express();
const Port = 4000;
const request = require('request');

app.use(express.json());

app.get("/AllTickets",(req,res)=>{

    let options = {
        url:"https://magical.atlassian.net/rest/api/latest/search",
        auth:{
            user:"bhumeshkewat10@gmail.com",
            password:"ATATT3xFfGF0dHNXKDCNhX737PaFltEPNpsbw36QA3wwMqiLcUlfs03Au0aqZ-YpHuVX47YdOHngFp7CJgJjLmbnfyDnxiMxiRtMN7M9hr3FeoADsGG6MtiqIOMhP6zRRheTzoXoGo7m9Q-8GYBEBkpR33pB_dIJg6CPhjEmF1Hlgow_Pcjp6q0=E6A1E44E"
        },
        qs:{
            jql:"project=JIR"
        }
    }
    request(options,(err,Response,body)=>{
        if(Response.statusCode === 200){
            res.status(200).json({message:"Ticket Fetched Successfully...",Ticket:JSON.parse(body)})
        }else{
            res.status(500).json({message:err})
        }
    })
})

app.post("/CreateTicket",(req,res)=>{

    let info = req.body
    const options2 = {
        method: 'POST',
        url: 'https://magical.atlassian.net/rest/api/latest/issue',
        auth: {
            user: 'bhumeshkewat10@gmail.com',
            password: 'ATATT3xFfGF0dHNXKDCNhX737PaFltEPNpsbw36QA3wwMqiLcUlfs03Au0aqZ-YpHuVX47YdOHngFp7CJgJjLmbnfyDnxiMxiRtMN7M9hr3FeoADsGG6MtiqIOMhP6zRRheTzoXoGo7m9Q-8GYBEBkpR33pB_dIJg6CPhjEmF1Hlgow_Pcjp6q0=E6A1E44E'
        },
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(info)
    };
    request(options2,(err,response,body)=>{
        if(response.statusCode === 201){
            res.status(201).json({message:"Tickit Created Successfully..."})
        }else{
            res.status(500).json({message:err})
        }
    })
})


app.patch("/updateTicket",(req,res)=>{

    const options3 = {
        method: 'POST',
        url: 'https://magical.atlassian.net/rest/api/latest/issue/JIR-5/transitions',
        auth: {
            user: 'bhumeshkewat10@gmail.com',
            password: 'ATATT3xFfGF0dHNXKDCNhX737PaFltEPNpsbw36QA3wwMqiLcUlfs03Au0aqZ-YpHuVX47YdOHngFp7CJgJjLmbnfyDnxiMxiRtMN7M9hr3FeoADsGG6MtiqIOMhP6zRRheTzoXoGo7m9Q-8GYBEBkpR33pB_dIJg6CPhjEmF1Hlgow_Pcjp6q0=E6A1E44E'
        },
        headers: {
            'Content-Type':'application/json'
        },      
        body: JSON.stringify({
            "transition": {
                "id": "11"
            }
        })
    };
    request(options3, function(error, response, body) {
        if(response.statusCode === 204){
            res.status(204).json({message:"Tickit Status Updated Successfully..."})
        }else{
            res.status(500).json({message:error})
        }
    });
})


app.delete("/DeleteTicket",(req,res)=>{

    const options4 = {
        method: 'DELETE',
        url: 'https://magical.atlassian.net/rest/api/latest/issue/JIR-13',
        auth: {
            user: 'bhumeshkewat10@gmail.com',
            password: 'ATATT3xFfGF0dHNXKDCNhX737PaFltEPNpsbw36QA3wwMqiLcUlfs03Au0aqZ-YpHuVX47YdOHngFp7CJgJjLmbnfyDnxiMxiRtMN7M9hr3FeoADsGG6MtiqIOMhP6zRRheTzoXoGo7m9Q-8GYBEBkpR33pB_dIJg6CPhjEmF1Hlgow_Pcjp6q0=E6A1E44E'
        },
        headers: {
            'Content-Type': 'application/json'
        }
    };
    request(options4,(error, response, body)=>{

        if(response.statusCode === 204){
            res.status(204).json({message:'Ticket deleted successfully.'})
        }else{
            res.status(500).json({message:error})
        }
    });
})

app.listen(Port,()=>{
    console.log(`my server running at http://localhost:${Port}`)
})