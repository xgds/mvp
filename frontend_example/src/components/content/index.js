import "./style.css";
import React from "react";

import {
    Card, 
    CardHeader,
    CardBody, 
    CardFooter,
    Button,
} from 'reactstrap';

import HeaderDropdownGroup from "../headerDropdownGroup";

class CardContent extends React.Component {
    render() {
        let header = undefined;
        if (this.props.header) {
            header = (
                <CardHeader className="card-center">
                    <HeaderDropdownGroup />
                </CardHeader>
            );
        }

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
                {header}
                <CardBody>
                    {this.props.content}
                </CardBody>
                {footer}
            </Card>
        );
    }
}

class Content extends React.Component {
    render() {
        return (
            <CardContent 
                className="content"
                content={this.props.content}
                footer={this.props.footer}
                header={this.props.header}
                store={this.store}
            />
        );
    }
}

export default Content;
