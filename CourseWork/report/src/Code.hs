module DFA
( DFA (..)
, trans
, run
, accept
) where

import qualified Data.Map as Map
import qualified Data.Set as Set
import Data.Maybe
import Control.Monad

type Delta s a = Map.Map (s, a) s

data DFA s a = DFA
    { states :: Set.Set s
    , sigma :: Set.Set a
    , delta :: Delta s a
    , startState :: s
    , acceptStates :: Set.Set s
    } deriving (Show)

trans :: (Ord s, Ord a) => s -> a -> DFA s a -> Maybe s
trans state alpha dfa = Map.lookup (state, alpha) $ delta dfa

run :: (Ord s, Ord a) => [a] -> DFA s a -> Maybe s
run input dfa = (foldM trans' $ startState dfa) input
    where trans' state alpha = trans state alpha dfa

accept :: (Ord s, Ord a) => [a] -> DFA s a -> Bool
accept input dfa =
    if isNothing $ final
        then False
        else Set.member (fromJust final) (acceptStates dfa)
    where final = run input dfa