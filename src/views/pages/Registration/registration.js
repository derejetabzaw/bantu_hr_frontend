import React from 'react'
import { Link } from 'react-router-dom'
import { Container,Form,Button,Card,InputGroup,FormControl,Row,Col,DropdownButton,Dropdown } from 'react-bootstrap';

const Registration = ()=>{
    return (
        <div style={{marginLeft:'auto',marginRight:'auto',marginTop:'5%'}}>

        <Container>
            <Card style={{marginBottom:'2%',border: '3px solid #D3DEDC'}}> 
                <h2 style={{padding:'4px',marginLeft:'auto',marginRight:'auto'}}>Add Employee</h2>
            </Card>
        <Card style={{padding:'10px',border: '3px solid #D3DEDC'}}>
            <Row>
                
             
           
                <Col>
                    <Form.Label>First Name</Form.Label>
                    <InputGroup>
                    <FormControl />
                    </InputGroup>
                </Col>
                
                <Col>
                <Form.Label>Last name</Form.Label>
                <InputGroup>
                <FormControl />
                </InputGroup>
                </Col>
            </Row>
            
            <Row>
                <Col>
                <Form.Label>Job Title</Form.Label>
                  <InputGroup>
                    <FormControl />
                  </InputGroup>
                </Col>
            </Row>
            
            <Row>
                
                <Col>
                <Form.Label>Employement</Form.Label>
                    <InputGroup>
                        <FormControl />
                    </InputGroup>
                </Col>
                 
                <Col>
                <Form.Label>payGrade</Form.Label>
                    <InputGroup>
                        <FormControl />
                    </InputGroup>
                </Col>
                
            </Row>
            <h2 style={{padding:'4px',marginLeft:'auto',marginRight:'auto'}}>Additional Information</h2>
            <Row>
                <Col>
                    <Form.Label>Email</Form.Label>
                    <InputGroup>
                        <FormControl/>
                    </InputGroup>
                </Col>
                <Col>
                    <Form.Label>Telephone</Form.Label>
                    <InputGroup>
                        <FormControl/>
                    </InputGroup>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Form.Label>Gender</Form.Label>
                      <InputGroup className="mb-3">
    <DropdownButton
      variant="outline-secondary"
      title="Gender"
      id="input-group-dropdown-1"
    >
      <Dropdown.Item href="#">Female</Dropdown.Item>
      <Dropdown.Item href="#">Male</Dropdown.Item>
    </DropdownButton>
    
  </InputGroup>
                </Col>
                <Col>
                <Form.Label>Adress</Form.Label>
                <InputGroup>
                    <FormControl />
                </InputGroup>
                </Col>
            </Row>
                <Button>Add Employee</Button>
            </Card>
        
            </Container>
            </div>
           
        

    )
}

export default Registration