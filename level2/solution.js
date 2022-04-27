// function to calculate the commission of the user depending on his objective and the total amounts of his deals
const calculateCommission = (totalAmounts, objective) => {
  const amountUnder50Percent =
    totalAmounts > 0.5 * objective ? 0.5 * objective : totalAmounts;
  const amountOver50Under100Percent =
    totalAmounts >= objective ? 0.5 * objective : 0;
  const amountOver100Percent =
    totalAmounts > objective ? totalAmounts - objective : 0;
  return (
    amountUnder50Percent * 0.05 +
    amountOver50Under100Percent * 0.1 +
    amountOver100Percent * 0.15
  );
};

const data = require("./data/input.json");

const users = data["users"];
const deals = data["deals"];

let result = { commissions: [] };

users.map((user) => {
  let totalAmounts = 0;
  deals.map((deal) => {
    if (deal.user === user.id) {
      totalAmounts += deal.amount;
    }
  });
  const commission = calculateCommission(totalAmounts, user.objective);
  result.commissions.push({ user_id: user.id, commission: commission });
});
