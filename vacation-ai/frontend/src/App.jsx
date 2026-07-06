import { useState } from "react";

function App() {
  const [tripCategory, setTripCategory] = useState("");
  const [travelWith, setTravelWith] = useState("");
  const [purpose, setPurpose] = useState("");
  const [budget, setBudget] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const [recommendations, setRecommendations] = useState([]);

  const getRecommendations = async () => {
    const response = await fetch(
      `http://127.0.0.1:8000/recommend?trip_category=${tripCategory}&travel_with=${travelWith}&purpose=${purpose}&budget=${budget}&start_date=${startDate}&end_date=${endDate}`
    );

   const data = await response.json();

   console.log("API Response:", data);

   setRecommendations(data);
  };

  return (
    <div className="form-section">

  <h3>Trip Type</h3>

  <div className="radio-group">
    <label>
      <input
        type="radio"
        value="domestic"
        checked={tripCategory === "domestic"}
        onChange={(e) => setTripCategory(e.target.value)}
      />
      🇮🇳 Domestic
    </label>

    <label>
      <input
        type="radio"
        value="international"
        checked={tripCategory === "international"}
        onChange={(e) => setTripCategory(e.target.value)}
      />
      🌎 International
    </label>
  </div>

  <div className="form-group">
    <h3>Travel With</h3>

    <select
      value={travelWith}
      onChange={(e) => setTravelWith(e.target.value)}
    >
      <option value="">Select</option>
      <option value="solo">👤 Solo</option>
      <option value="partner">❤️ Partner</option>
      <option value="family">👨‍👩‍👧 Family</option>
      <option value="friends">🎉 Friends</option>
    </select>
  </div>

  <div className="form-group">
    <h3>Purpose</h3>

    <select
      value={purpose}
      onChange={(e) => setPurpose(e.target.value)}
    >
      <option value="">Select</option>
      <option value="honeymoon">❤️ Honeymoon</option>
      <option value="adventure">⛰️ Adventure</option>
      <option value="relaxation">🏖️ Relaxation</option>
      <option value="culture">🏛️ Culture</option>
    </select>
  </div>

  <div className="form-group">
    <h3>Budget</h3>

    <select
      value={budget}
      onChange={(e) => setBudget(e.target.value)}
    >
      <option value="">Select</option>
      <option value="low">💰 Low</option>
      <option value="medium">💰💰 Medium</option>
      <option value="high">💰💰💰 High</option>
    </select>
  </div>

  <div className="date-row">
    <div>
      <h3>Start Date</h3>
      <input
        type="date"
        value={startDate}
        onChange={(e) => setStartDate(e.target.value)}
      />
    </div>

    <div>
      <h3>End Date</h3>
      <input
        type="date"
        value={endDate}
        onChange={(e) => setEndDate(e.target.value)}
      />
    </div>
  </div>

  <button className="search-btn" onClick={getRecommendations}>
    ✈️ Find My Vacation
  </button>
  {recommendations.map((place, index) => (
  <div
    key={index}
    className="destination-card"
  >
    <div className="results-section">
  {recommendations.map((place, index) => (
    <div
      key={index}
      className="destination-card"
      style={{
        backgroundImage: `url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200")`
      }}
    >
      <div className="card-overlay">
        <div className="card-content">
          <h2>📍 {place.destination}</h2>

          <p>🌍 {place.country}</p>

          <div className="score-badge">
            ⭐ Match Score: {place.score}
          </div>

          <div className="tags">
            <span>🏖️ Beaches</span>
            <span>🎭 Culture</span>
            <span>🌿 Nature</span>
          </div>
        </div>
      </div>
    </div>
  ))}
</div>
  </div>
))}

</div>
  );
}

export default App;