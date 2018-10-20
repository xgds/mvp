import React from "react";
import HeaderDropdownGroup from "../headerDropdownGroup";

import {
    Card, CardHeader,
    CardBody, CardFooter,
    Button,
} from 'reactstrap';

import "./style.css";

class CardContent extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
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
                <CardHeader className="card-center">
                    <HeaderDropdownGroup />
                </CardHeader>
                <CardBody>
                    {content}
                </CardBody>
                {footer}
            </Card>
        );
    }
}

export default CardContent;