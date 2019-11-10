import React, { Component , Fragment} from 'react'
import {connect } from 'react-redux';
import PropTypes from 'prop-types';
import {getOffers, deleteOffer} from '../../actions/offers';
import { AUTH_ERROR } from '../../actions/types';

export class Offers extends Component {
    static propTypes = {
        name: PropTypes.string,
        id:PropTypes.number,
        offers: PropTypes.array.isRequired,
        getOffers: PropTypes.func.isRequired,
        deleteOffer: PropTypes.func.isRequired


      
      };
      componentDidMount() {
        this.props.getOffers(this.props.id);
      }
      

    render() {
        return (
            <Fragment>
            <h2>Registred Offers</h2>
            <table className="table table-striped">
              <thead>
                <tr> 
                  <th>ID</th>
                  <th>Name</th>
                  <th>Description</th>
                  <th>Number of positions</th>
                  <th>People who applied</th>
                  <th>Creation date</th>
                  <th>Expiration date</th>
                  <th>Status</th>
                  <th />
                </tr>
              </thead>
              <tbody>
                {this.props.offers.map(offer => (
                  <tr key={offer.id}>
                    <td>{offer.id}</td>
                    <td>{offer.name}</td>
                    <td>{offer.description}</td>
                    <td>{offer.nb_places}</td>
                    <td>{offer.nb_applicants}</td>
                    <td>{offer.CreationDate}</td>
                    <td>{offer.ExpDate}</td>
                    <td>{offer.Status}</td>
                    <td>
                    <button onClick={this.props.deleteOffer.bind(this,offer.id)} className="btn btn-danger btn-sm"
>

                        {" "}
                        Delete
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    offers: state.offers.offers,
    name :  state.auth.user.name,
    id : state.auth.user.id
  });
export default connect(mapStateToProps, {getOffers, deleteOffer})(Offers)
