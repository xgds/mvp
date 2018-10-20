import React from "react";
import {
    Button,
} from 'reactstrap';

class MapPopover extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            text: "",
        }
    }

    componentDidMount() {
        this.props.popoverStore.subscribe(function () {
            this.setState({
                text: this.props.popoverStore.getState().text,
            });
        }.bind(this));
    }

    render() {
        return (
            <Button id="popoverButton">
                {this.state.text}
            </Button>
        );
    }

}

export default MapPopover;