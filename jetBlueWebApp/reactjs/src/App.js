import './App.css'
import OpenModal from './components/OpenModal'
import 'react-bulma-components/dist/react-bulma-components.min.css'
import { Container, Button, Hero, Heading, Columns, Message, Modal, Section } from 'react-bulma-components'

import React, {Component} from 'react'

class App extends Component {
  render() {
    return <Container>
      <Hero color="primary">
        <Hero.Body>
          <Container>
            <Heading>
              <span className="brand-title">AirMetrics</span>
            </Heading>
            <Heading subtitle>
              Actionable insights for you and your airline
            </Heading>
            <OpenModal modal={{ closeOnEsc : true }}>
              <Modal.Content>
                <Section style={{ backgroundColor : 'white'}}>
                  <p>Airlines</p>
                </Section>
              </Modal.Content>
            </OpenModal>
          </Container>
        </Hero.Body>
      </Hero>
      <Columns>
        <Columns.Column>
          <Message>
            <Message.Header>Specific</Message.Header>
              <Message.Body>
                We use categorized sentiment analysis to find and eliminate points of friction.
                <br /><br />
                <div className="has-text-centered">
                  <i className="fas fa-bullseye fa-10x"></i>
                </div>
              </Message.Body>
          </Message>
        </Columns.Column>
        <Columns.Column>
          <Message>
            <Message.Header>Visual</Message.Header>
            <Message.Body>
              We track sentiment over time and display it in pretty graphs.
              <br /><br /><i className="fa fa-chart-bar fa-10x"></i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <i className="fa fa-chart-line fa-10x"></i>
            </Message.Body>
          </Message>
        </Columns.Column>
        <Columns.Column>
          <Message>
            <Message.Header>Flexible</Message.Header>
            <Message.Body>
              Output can be exported in different formats.
              <br /><br /><br /><div className="has-text-centered">
              <i className="fas fa-file fa-10x"></i>
              </div>
            </Message.Body>
          </Message>
        </Columns.Column>

      </Columns>
    </Container>
  }
}

export default App
