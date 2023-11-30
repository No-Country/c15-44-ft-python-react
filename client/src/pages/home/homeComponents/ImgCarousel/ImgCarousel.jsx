import React from 'react';
import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';

const Pepe = () => {
  const images = [
    'https://picsum.photos/id/237/200/300',
    'https://picsum.photos/id/247/200/300',
    'https://picsum.photos/id/257/200/300',
    'https://picsum.photos/id/247/200/300',
    'https://picsum.photos/id/237/200/300',
  ];

  const responsive = {
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 3,
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 2,
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1,
    },
  };

  return (
    <Carousel responsive={responsive}>
      {images.map((image, index) => (
        <div key={index}>
          <img src={image} alt={`Image ${index + 1}`} />
        </div>
      ))}
    </Carousel>
  );
};

export default Pepe;
