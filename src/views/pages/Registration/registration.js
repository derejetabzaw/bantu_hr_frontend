import { React,useState } from 'react'
import { Link } from 'react-router-dom'
import { Container,Form,Button,Card,InputGroup,
    FormControl,Row,Col,
    DropdownButton,Dropdown,
    Modal,Table } from 'react-bootstrap';

const Registration = ()=>{
    const [show,setShow] = useState(false);
    
    
    const handleClose= () => setShow(false)
    const handleShow = () => setShow(true)
   
   
        
    
    return (
        <>
    

<Modal show={show} onHide = {handleClose}>
           
            <Modal.Title>
                 
                <h3 style={{padding:'4px'}}>Add Employee</h3>
            
            </Modal.Title>
            <Modal.Body style={{marginLeft:'0px'}}>
                
           
        
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
            <h3 style={{padding:'4px'}}>Additional Information</h3>
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
                <Button onClick={handleClose}>Add Employee</Button>
            </Modal.Body>
        </Modal>

<div style={{marginLeft:'auto',marginRight:'auto',}}>
<Container>
<Row>
    <Col>
        <Button onClick={()=>{handleShow()}} style={{float:'right',marginTop:'5%',marginBottom:'2%'}}>Add Employee</Button>
    </Col>
</Row>
    </Container>
    
 <Container>    
<Table responsive>
  <thead>
    <tr>
      <th>#</th>
      {Array.from({ length: 12 }).map((_, index) => (
        <th key={index}>Table heading</th>
      ))}
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      {Array.from({ length: 12 }).map((_, index) => (
        <td key={index}>Table cell {index}</td>
      ))}
    </tr>
    <tr>
      <td>2</td>
      {Array.from({ length: 12 }).map((_, index) => (
        <td key={index}>Table cell {index}</td>
      ))}
    </tr>
    <tr>
      <td>3</td>
      {Array.from({ length: 12 }).map((_, index) => (
        <td key={index}>Table cell {index}</td>
      ))}
    </tr>
  </tbody>
</Table>
</Container>
</div>

    </>
      
    )
    }
export default Registration