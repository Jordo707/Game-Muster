import React, { useState } from 'react';

const Dice = () => {
    const [displayRolls, setDisplayRolls] = useState([]);
    const [rolls, setRolls] = useState([]);
    const [numberOfDice, setNumberOfDice] = useState(1);
    const [diceType, setDiceType] = useState(6);

    const rollDice = () => {
      // Clear any ongoing animation
      setDisplayRolls([]);

      // Start animation
      const interval = setInterval(() => {
        const randomRolls = Array.from({ length: numberOfDice }, () => Math.floor(Math.random() * diceType) + 1);
        setDisplayRolls(randomRolls);
      }, 100);

      // Stop animation and show final result after 1 to 2 seconds
      setTimeout(() => {
        clearInterval(interval);
        const finalRolls = Array.from({ length: numberOfDice }, () => Math.floor(Math.random() * diceType) + 1);
        setRolls(finalRolls);
        setDisplayRolls(finalRolls);
      }, 1000 + Math.random() * 1000);
    };

    // Calculate the total of the final rolls
    const totalRoll = rolls.reduce((acc, current) => acc + current, 0);

    return (
      <div>
        <div>
          <label htmlFor="dice-number">Number of Dice: </label>
          <select id="dice-number" value={numberOfDice} onChange={(e) => setNumberOfDice(Number(e.target.value))}>
            {[...Array(10).keys()].map(n => (
              <option key={n + 1} value={n + 1}>{n + 1}</option>
            ))}
          </select>
        </div>

        <div>
          <label htmlFor="dice-type">Type of Dice: </label>
          <select id="dice-type" value={diceType} onChange={(e) => setDiceType(Number(e.target.value))}>
            {[4, 6, 10, 20, 100].map(type => (
              <option key={type} value={type}>{`d${type}`}</option>
            ))}
          </select>
        </div>

        <button onClick={rollDice}>Roll Dice</button>
        {displayRolls.length > 0 && (
          <div>
            <h2>Rolls: {displayRolls.join(', ')}</h2>
            {/* Show total only after final rolls are determined */}
            {rolls.length === displayRolls.length && <h3>Total: {totalRoll}</h3>}
          </div>
        )}
      </div>
    );
};

export default Dice;
