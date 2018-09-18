import React from "react";
import {
    Card, CardHeader,
    CardBody, CardFooter, CardTitle, CardText,
    ListGroup, ListGroupItem, ListGroupItemHeading, ListGroupItemText,
    Button,
    Dropdown, DropdownMenu, DropdownItem, DropdownToggle,
} from 'reactstrap';

class HeaderDropdown extends React.Component {
    constructor(props) {
        super(props);

        this.toggle = this.toggle.bind(this);
        this.state = {
            dropdownOpen: false
        };
    }

    toggle() {
        this.setState(prevState => ({
            dropdownOpen: !prevState.dropdownOpen
        }));
    }

    render() {
        return (
            <Dropdown isOpen={this.state.dropdownOpen} toggle={this.toggle}>
                <DropdownToggle caret>
                    Dropdown
                </DropdownToggle>
                <DropdownMenu>
                    <DropdownItem header>Header</DropdownItem>
                    <DropdownItem disabled>Action</DropdownItem>
                    <DropdownItem>Another Action</DropdownItem>
                    <DropdownItem divider />
                    <DropdownItem>Another Action</DropdownItem>
                </DropdownMenu>
            </Dropdown>
        );
    }
}

export default HeaderDropdown;