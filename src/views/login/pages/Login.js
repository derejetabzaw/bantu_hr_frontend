import React from 'react'
import { Link } from 'react-router-dom'
import { Container,Form,Button,Card,InputGroup,FormControl,Row,Col } from 'react-bootstrap';
import { CIcon } from '@coreui/icons-react';
import img from './dummy.jpg'

const Login = ()=>{
   return (
  <div className="c-app c-default-layout flex-row align-items-center" style={{marginTop:'5%'}}>
  <Container fluid>
    <Row className="justify-content-center">
      <Col md="8">
    <Card style={{border: '2px solid #D3DEDC'}} className="p-4">
   <Card.Img src={img} style={{borderRadius :'50%',height:'200px',width:'200px',marginLeft:'auto',marginRight:'auto',display:'block',paddingBottom:'4px'}} ></Card.Img>
     <Form>
       <InputGroup className="mb-3" size='sm'>
       <InputGroup.Text id="basic-addon1"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person" viewBox="0 0 16 16">
  <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/>
</svg></InputGroup.Text>
       <FormControl
      placeholder="Username"
   
    />
  </InputGroup>

  <InputGroup size="sm" className="mb-3">
    <InputGroup.Text id="inputGroup-sizing-sm"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lock" viewBox="0 0 16 16">
  <path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2zM5 8h6a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/>
</svg></InputGroup.Text>
    <FormControl aria-label="Small" aria-describedby="inputGroup-sizing-sm" 
     placeholder="Password"
    />
  </InputGroup>
  <Button variant="primary" type="submit">
    Login
  </Button>
  <a href='#' style={{float:'right'}}>forgot password ?</a>
</Form>
</Card>
</Col>
</Row>

       </Container>
       </div>
  )
}

export default Login
