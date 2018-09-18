import React from "react";

import {
    Card, CardHeader,
    CardBody, CardFooter, CardTitle, CardText,
    ListGroup, ListGroupItem, ListGroupItemHeading, ListGroupItemText,
    Button,
    Dropdown, DropdownMenu, DropdownItem, DropdownToggle,
} from 'reactstrap';

import CardContentTable from "../cardContentTable";
import HeaderDropdownGroup from "../headerDropdownGroup";

import $ from "jquery";

class TabularContent extends React.Component {
    componentDidMount() {
        $(".ReactTable").height($(".card-body").height());
    }

    render() {
        let content = (
            <CardContentTable
                store={this.props.store}
            />
        );

        let footer = undefined;
        if (this.props.footer) {
            footer = (
                <CardFooter className="card-center">
                    <Button color="primary">primary</Button>
                    <Button color="secondary">secondary</Button>
                    <Button color="success">success</Button>
                </CardFooter>
            );
        }

        return (
            <Card>
                <CardHeader className="card-center"><HeaderDropdownGroup /></CardHeader>
                <CardBody>{content}</CardBody>
                {footer}
            </Card>
        );
    }
}

export default TabularContent;
