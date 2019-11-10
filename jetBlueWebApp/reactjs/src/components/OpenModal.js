import React, { Component } from 'react';
import PropTypes from 'prop-types';
import 'react-bulma-components/dist/react-bulma-components.min.css';
import { Button, Modal } from 'react-bulma-components';

class OpenModal extends React.Component {
    static propTypes = {
        modal : PropTypes.object,
        children : PropTypes.node.isRequired
    }

    static defaultProps = {
        modal : {},
    }

    state = {
        show : false,
    }

    open = () => this.setState({ show : true});
    close = () => this.setState({ show : false});

    render() {
        return (
            <div>
                <Button outlined={true} rounded={true} onClick={this.open}>Select Airline</Button>
                <Modal show={this.state.show} onClose={this.close} {...this.props.modal}>
                    {this.props.children}
                </Modal>
            </div>
        );
    }
}

export default OpenModal;